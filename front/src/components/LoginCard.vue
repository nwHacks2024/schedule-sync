<template>
    <div class="column q-pa-lg">
      <div class="row">
        <q-card square class="shadow-24" style="width:300px;height:500px;">
          <q-card-section class="bg-deep-purple-7">
            <h4 class="text-h5 text-white q-my-md">Login to BDEC</h4>
          </q-card-section>
          <q-card-section>
            <q-form class="q-px-sm q-pt-xl">
              <q-input square clearable v-model="username" type="username" label="Username">
                <template v-slot:prepend>
                  <q-icon name="person" />
                </template>
              </q-input>
              <q-input square clearable v-model="password" type="password" label="Password">
                <template v-slot:prepend>
                  <q-icon name="lock" />
                </template>
              </q-input>
            </q-form>
          </q-card-section>
          <q-card-actions class="q-px-lg">
            <!-- Back and Sign In buttons within the same q-card-actions section -->
            <q-btn unelevated size="lg" color="green-4" class="full-width text-white" label="Back" @click="goBack" />
            <q-btn unelevated size="lg" color="purple-4" class="full-width text-white" label="Sign In" @click="login" />
          </q-card-actions>
        </q-card>
      </div>
    </div>

</template>

<script>
import axios from "axios";
import {useRouter} from "vue-router";
import {useAuthStore} from "src/stores";

export default {
  name: 'LoginCard',
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    async login() {
      try {
        // Make an HTTP POST request to the /api/login endpoint
        const response = await axios.post('/api/login', {
          username: this.username,
          password: this.password,
        });

        // Handle the response as needed
        console.log('User logged in successfully:', response.data);
        useAuthStore().setUsername(this.username);
        this.$router.push('/main');
      } catch (error) {
        // Handle errors
        console.error('Incorrect credentials:', error.response ? error.response.data : error.message);
      }
    },
    goBack() {
      this.$emit('goBack');
    }
  }
}
</script>

<style>
</style>
