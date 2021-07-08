<template>
  <div class="hello" @click.prevent="downloadItem(file)">
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
        .then((response) => {
          const blob = new Blob([response.data], { type: "application/pdf" });
          const link = document.createElement("a");
          link.href = URL.createObjectURL(blob);
          link.download = name;
          link.click();
          URL.revokeObjectURL(link.href);
        })
        .catch(console.error);
    },
  },
};
</script>
