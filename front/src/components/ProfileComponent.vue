<template>
  <div class="profile-page">
    <div class="profile-card">
      <q-spinner-gears v-if="loading" size="50px"></q-spinner-gears>

      <img class="avatar" v-else src="/public/icons/defaultprofile.png" alt="User Avatar" />
      <h2 class="username" v-if="!loading">{{ userProfile.username }}</h2>
      <p class="firstName" v-if="!loading">{{ userProfile.firstName }}</p>
      <p class="lastName" v-if="!loading">{{ userProfile.lastName }}</p>
      <p class="faculty" v-if="!loading">{{ userProfile.faculty }}</p>
      <p class="degreeName" v-if="!loading">{{ userProfile.degreeName }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      userProfile: {
        username: '',
        firstName: '',
        lastName: '',
        faculty: '',
        degreeName: '',
      },
      loading: true, // Set loading to true initially
    };
  },
  mounted() {
    this.fetchUserProfile();
  },
  methods: {
    async fetchUserProfile() {
      try {
        // Assuming the /api/userprofile endpoint returns the user profile data
        const response = await axios.post('/api/userprofile', {
          username: 'dfroberg',
        });
        const userData = response.data;

        // Update the userProfile data with the data from the API
        this.userProfile.username = userData.username;
        this.userProfile.email = userData.email;
        this.userProfile.firstName = userData.firstName;
        this.userProfile.lastName = userData.lastName;
        this.userProfile.faculty = userData.faculty;
        this.userProfile.degreeName = userData.degreeName;
      } catch (error) {
        console.error('Error fetching user profile:', error);
      } finally {
        this.loading = false; // Set loading back to false regardless of success or error
      }
    },
  },
};
</script>

<style scoped>
.profile-page {
  height: 100vh;
  background-color: #f5f5f5;
}

.profile-card {
  width: 100%;
  height: 100%;
  background-color: #ffffff;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: center;
}

.avatar {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  margin-bottom: 10px;
}

.username {
  font-size: 1.5em;
  margin-bottom: 5px;
}

.email {
  color: #555555;
  margin-bottom: 20px;
}

.info {
  text-align: left;
}

/* Add more styles as needed */
</style>
