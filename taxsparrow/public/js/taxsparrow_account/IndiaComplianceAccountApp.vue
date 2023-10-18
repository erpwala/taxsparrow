<template>
  <div class="tax-sparrow">
    <transition name="fade">
      <div class="content">
          <PreLoader v-if="isLoading" />
          <transition name="fade" mode="out-in" v-else>
            <router-view />
          </transition>
      </div>
    </transition>
    <TheFooter />
  </div>
</template>

<script>
import PreLoader from "./components/PreLoader.vue";
import TheFooter from "./components/TheFooter.vue";

export default {
  components: { PreLoader, TheFooter },

  data() {
    return {
      isLoading: true,
    };
  },

  watch: {
    async $route() {
      frappe.router.current_route = await frappe.router.parse();
      frappe.breadcrumbs.update();
    },
  },

  async created() {
    await this.$store.dispatch("initAuth");
    this.isLoading = false;
  },
};
</script>

<style scoped>
.tax-sparrow {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
}

.tax-sparrow > .content {
  flex-grow: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
