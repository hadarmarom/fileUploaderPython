<template>
  <div id="app">
    <h1>Save & Download Files Here!</h1>
    <div class="btns-containet">
      <label class="file-input-label" for="file">Enter File Here</label>
      <input
        type="file"
        id="file"
        ref="files"
        class="file-input"
        @change="previewFiles"
        multiple
      />
    <button class="submit-btn" @click="submitFiles()">Submit</button>
    </div>

    <ul class="file-list">
      <div v-if="files.length && !filesToSave.length">
        <div><h1>Saved Files:</h1></div>
        <li v-for="(file, idx) in files" :key="idx">
          <file-preview :file="file" />
        </li>
      </div>
      <div v-if="filesToSave.length">
        <h1>Current Files Chosed:</h1>
        <li v-for="(file, idx) in filesToSave" :key="idx">
          <div>{{ file.name }}</div>
        </li>
      </div>
    </ul>
  </div>
</template>

<script>
import axios from "axios";
import filePreview from "./cmps/file-preview.vue";

export default {
  name: "App",
  data() {
    return {
      files: [],
      filesToSave: [],
      fileSrc: null,
      path: "http://localhost:5000/",
    };
  },
  async created() {
    axios
      .get(this.path)
      .then((res) => {
        var fromDataFiles = res.data;
        console.log('fromDataFiles:', fromDataFiles)
        if (fromDataFiles) this.files = fromDataFiles;
      })
      .catch((error) => {
        console.error(error);
      });
  },
  methods: {
    previewFiles() {
      this.filesToSave = [...Object.values(this.$refs.files.files)];
      const newFiles = this.$refs.files.files;
      newFiles.forEach((currFile, idx) => {
        const reader = new FileReader();
        reader.readAsDataURL(currFile);
        reader.onload = (ev) => {
          this.fileSrc = ev.target.result;
          this.filesToSave[idx].fileSrc = ev.target.result;
        };
      });
    },
    async submitFiles() {
      let formData = new FormData();
      for (var i = 0; i < this.filesToSave.length; i++) {
        let file = this.filesToSave[i];
        formData.append("files[" + i + "]", file);
        this.filesToSave.forEach((file) => {
          var modifiedFile = {
            name: file.name,
            fileSrc: file.fileSrc,
          };
          axios
            .post("http://localhost:5000/", modifiedFile)
            .then(() => {
              axios
                .get(this.path)
                .then((res) => {
                  var fromDataFiles = res.data;
                  if (fromDataFiles) this.files = fromDataFiles;
                  this.filesToSave = [];
                })
                .catch((error) => {
                  console.error(error);
                });
            })
            .catch((error) => {
              this.errorMessage = error.message;
              console.error("There was an error!", error);
            });
        });
      }
    },
  },
  components: {
    filePreview,
  },
};
</script>
