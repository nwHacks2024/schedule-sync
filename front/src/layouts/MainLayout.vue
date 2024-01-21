<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white" height-hint="98">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg" />
          </q-avatar>
          BDEC
        </q-toolbar-title>

        <q-btn dense flat round icon="menu" @click="toggleRightDrawer" />
      </q-toolbar>

      <q-tabs align="left">
        <q-route-tab to="/" label="Home" />
        <q-route-tab to="/page1" label="Your Schedule" />
        <q-route-tab to="/page2" label="Degree Navigator" />
        <q-route-tab to="/page3" label="Friend Schedules" />
        <FriendsDropdown />
      </q-tabs>
    </q-header>

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-grey-8 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <q-avatar>
            <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg" />
          </q-avatar>
          <div>BDEC</div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>

    <q-drawer
      show-if-above
      v-model="rightDrawerOpen"
      side="right"
      bordered
      class="my-drawer bg-secondary"
    >
     <MenuComponent />
    </q-drawer>
  </q-layout>
</template>

<script>
import { ref } from "vue";
import MenuComponent from '../components/MenuComponent.vue'
import FriendsDropdown from "../components/FriendsDropdown.vue";

export default {
  components: {
    MenuComponent,
    FriendsDropdown
  },
  setup() {
    const rightDrawerOpen = ref(false);

    return {
      rightDrawerOpen,
      toggleRightDrawer() {
        rightDrawerOpen.value = !rightDrawerOpen.value;
      },
    };
  },
};
</script>
<style scoped>
.bubble-item {
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50px; /* Adjust the border-radius to make it more or less rounded */
  padding: 10px; /* Adjust the padding to control the size of the bubble */
  margin: 10px; /* Add margin for spacing between items */
}
.router-link {
  text-decoration: none; /* Remove underline */
  color: inherit; /* Inherit the color from the parent */
}
.center-text {
  text-align: center;
  margin: 0;
}
</style>
