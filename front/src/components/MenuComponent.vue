<template>
  <div>
    <!-- <q-list>
      <router-link to="/friends" class="router-link">
        <q-item clickable v-ripple style="height: 60px" class="bubble-item">
          <q-item-section>
            <q-item-label class="center-text">Friends</q-item-label>
          </q-item-section>
          <q-item-section>
            <q-icon name="person" size="lg" />
          </q-item-section>
        </q-item>
      </router-link>

    </q-list> -->
    <ProfileComponent />
  </div>

  <!-- <DisplayFriends /> -->
</template>

<script>
import { ref } from "vue";
import ProfileComponent from "../components/ProfileComponent.vue";


export default {
  components: {
    ProfileComponent
  },
};
</script>
