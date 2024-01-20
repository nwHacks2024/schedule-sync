<template>
    <q-layout view="hHh lpR fFf">
  
      <q-header elevated class="bg-primary text-white" height-hint="98">
        <q-toolbar>

          <q-toolbar-title>
            <q-avatar>
              <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
            </q-avatar>
            BDEC
          </q-toolbar-title>
        </q-toolbar>
  
      </q-header>
  
      <q-page-container>
        <router-view />
      </q-page-container>
  
      <q-footer elevated class="bg-grey-8 text-white">
        <q-toolbar>
          <q-toolbar-title>
            <q-avatar>
              <img src="https://cdn.quasar.dev/logo-v2/svg/logo-mono-white.svg">
            </q-avatar>
            <div>BDEC</div>
          </q-toolbar-title>
        </q-toolbar>
      </q-footer>
  
    </q-layout>
  </template>
  
  <script>
  import { ref } from 'vue'
  
  export default {
    setup () {
      const leftDrawerOpen = ref(false)
      const rightDrawerOpen = ref(false)
  
      return {
        leftDrawerOpen,
        toggleLeftDrawer () {
          leftDrawerOpen.value = !leftDrawerOpen.value
        },
  
        rightDrawerOpen,
        toggleRightDrawer () {
          rightDrawerOpen.value = !rightDrawerOpen.value
        }
      }
    }
  }
  </script>
  