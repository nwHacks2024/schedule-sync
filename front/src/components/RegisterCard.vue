<template>
      <div class="column q-pa-lg">
        <div class="row">
          <q-card square class="shadow-24" style="width:300px;height:550px;">
            <q-card-section class="bg-deep-purple-7">
              <h4 class="text-h5 text-white q-my-md">Registration</h4>
              <div class="absolute-bottom-right q-pr-md" style="transform: translateY(50%);">
                <q-btn fab icon="close" color="purple-4" />
              </div>
            </q-card-section>
            <q-card-section>
              <q-form class="q-px-sm q-pt-xl q-pb-lg">
                <q-input square clearable v-model="firstname" type="firstname" label="First Name">
                  <template v-slot:prepend>
                    <q-icon name="person" />
                  </template>
                </q-input>
                <q-input square clearable v-model="lastname" type="lastname" label="Last Name">
                  <template v-slot:prepend>
                    <q-icon name="person" />
                  </template>
                </q-input>
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
              <!-- Go Back button -->
              <q-btn unelevated size="lg" color="grey" class="full-width" label="Go Back" @click="goBack" />
              <!-- Register button -->
              <q-btn unelevated size="lg" color="purple-4" class="full-width text-white" label="Get Started" @click="register"/>
            </q-card-actions>
          </q-card>
        </div>
      </div>
  </template>

  <script>
  import axios from "axios";
  // import {useRouter} from "vue-router";

  export default {
  data() {
    return {
      firstname: '',
      lastname: '',
      username: '',
      password: '',
    };
  },
  methods: {
    async register() {
      try {
        // Make an HTTP POST request to the /api/register endpoint
        const response = await axios.post('/api/register', {
          firstName: this.firstname,
          lastName: this.lastname,
          username: this.username,
          password: this.password,
        });

        // Handle the response as needed
        console.log('User registered successfully:', response.data);
        this.$router.push('/main');
      } catch (error) {
        // Handle errors
        console.error('Error registering user:', error.response ? error.response.data : error.message);
      }
    },
    goBack() {
      this.$emit('goBack');

    },

  },
};
  </script>

