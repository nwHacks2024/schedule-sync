<template>
    <div class="column q-pa-lg">
      <div class="row">
        <q-card square class="shadow-24" style="width:300px;height:425px;">
          <q-card-section class="bg-deep-purple-7">
            <h4 class="text-h5 text-white q-my-md">Login to BDEC</h4>
          </q-card-section>
          <q-card-section>
            <q-form class="q-px-sm q-pt-xl">
              <q-input square clearable v-model="email" type="username" label="Username">
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
            <q-btn unelevated size="lg" color="purple-4" class="full-width text-white" label="Sign In" />
          </q-card-actions>
          <q-card-actions class="q-px-lg">
            <q-btn unelevated size="lg" color="green-4" class="full-width text-white" label="Back" />
          </q-card-actions>
        </q-card>
      </div>
    </div>

</template>

<script>
export default {
  name: 'LoginCard',
  data () {
    return {
      email: '',
      username: '',
      password: ''
    }
  },
  methods: {
    goBack() {
      this.isButtonClicked = false;
    }
  }
}
</script>

<style>
</style>