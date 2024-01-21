<template>
  <div class="container">
    <div v-if="!isButtonClicked">
      <button class='user-button' @click="showComponent('existing')">Existing User</button>
      <button class='user-button' @click="showComponent('new')">New User</button>
    </div>
    <LoginCard v-if="isButtonClicked && !isNewUser" />
    <RegisterCard v-if="isButtonClicked && isNewUser" />
    <button v-if="isButtonClicked" class="user-button" @click="goBack">Back</button>
  </div>
</template>

<script>
import LoginCard from '../components/LoginCard.vue'
import RegisterCard from '../components/RegisterCard.vue'
export default {
  components: {
    LoginCard,
    RegisterCard
  },
  data() {
    return {
      isNewUser: false,
      isButtonClicked: false
    }
  },
  methods: {
    showComponent(type) {
      this.isNewUser = type === 'new';
      this.isButtonClicked = true;
    },
    goBack() {
      this.isButtonClicked = false;
    }
  }
};
</script>

<style>
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  flex-direction: column;
}
.user-button {
  padding: 50px;
  font-size: 20px;
  color: white;
  background-color: #4CAF50; /* Change this to your preferred color */
  border: none;
  cursor: pointer;
  margin: 10px;
  border-radius: 5px;
  transition: background-color 0.3s;
}

.user-button:hover {
  background-color: #45a049; /* Change this to your preferred hover color */
}
</style>