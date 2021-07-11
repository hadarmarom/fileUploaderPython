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
      path: "http://localhost:5000/",
    };
  },
  async created() {
    this.getFiles();
  },
  methods: {
    previewFiles() {
      this.filesToSave = this.$refs.files.files;
      this.filesToSave.forEach((currFile) => {
        const reader = new FileReader(); // using a FileReader Object
        reader.readAsDataURL(currFile); // which read the contents of files
        reader.onload = (ev) => {
          currFile.fileSrc = ev.target.result;
        };
      });
    },
    async submitFiles() {
      this.filesToSave.forEach((file) => {
        var modifiedFile = { name: file.name, fileSrc: file.fileSrc };
        axios
          .post(this.path, modifiedFile)
          .then(() => {
            this.getFiles();
            this.filesToSave = [];
          })
          .catch((error) => {
            console.error("error in Post", error);
          });
      });
    },
    getFiles() {
      axios
        .get(this.path)
        .then((res) => {
          var fromDataFiles = res.data;
          if (fromDataFiles) this.files = fromDataFiles;
        })
        .catch((error) => {
          console.error("error in Get" + error);
        });
    },
  },
  components: {
    filePreview,
  },
};
</script>
