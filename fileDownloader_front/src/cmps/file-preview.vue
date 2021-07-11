<template>
  <div class="file-preview" @click.prevent="downloadItem(file)">
    {{ file.name }}
    <!-- <img :src="file.fileSrc" alt="File Image"> -->
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "filePreview",
  props: ["file"],
  methods: {
    downloadItem({ fileSrc, name }) {
      axios
        .get(fileSrc, { responseType: "blob" })
        .then(({ data }) => {
          //object of size and type of the file
          const link = document.createElement("a");
          const blob = new Blob([data], { type: "application/pdf" }); //Blob is a file-like object of immutable, raw data; it can be read as text or binary data
          link.href = URL.createObjectURL(blob); //creates a DOMString containing a URL of the object given
          link.download = name;
          link.click();
          URL.revokeObjectURL(link.href); //when finished- let the browser know not to keep the reference to the file any longer (like destroyed).
        })
        .catch(console.error);
    },
  },
};
</script>
