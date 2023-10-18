<template>
  <div class="loading-container">
    <h1>Tax Sparrow</h1>
    <h5>by Sparrownova</h5>
    <Loading :radius="40" class="mt-3" />
  </div>
</template>

<script>
import Loading from "./Loading.vue";

export default {
  components: { Loading },
};
</script>

<style scoped>
.loading-container {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
  height: calc(100vh - 60px);
}
</style>