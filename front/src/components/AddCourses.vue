<template>
  <div class="course-search">
    <q-select
      v-model="selectedDepartment"
      :options="departmentOptions"
      label="Select Department"
      @input="loadCourseNumbers"
    />

    <q-select
      v-model="selectedCourseNumber"
      :options="courseNumberOptions"
      label="Select Course Number"
      :disable="!selectedDepartment"
      @input="searchSections"
      class="q-mt-md"
    />

    <q-btn @click="searchSections" label="Search" color="primary" class="q-mt-md" />

    <q-carousel
      v-if="sections.length > 0"
      control-color="primary"
      arrows
      navigation
      infinite
    >
      <q-card v-for="section in sections" :key="section.id">
        <q-card-section>
          <q-card-title>{{ section.title }}</q-card-title>
        </q-card-section>
        <q-card-section>
          <p>{{ section.description }}</p>
        </q-card-section>
        <!-- Add more card content as needed -->
      </q-card>
    </q-carousel>

    <q-alert
      v-if="error"
      :type="errorType"
      :message="errorMessage"
      class="q-mt-md"
    />
  </div>
</template>

<script>
export default {
  data() {
    return {
      selectedDepartment: null,
      selectedCourseNumber: null,
      departmentOptions: [
        { label: 'CPSC', value: 'CPSC' },
        // Add more departments as needed
      ],
      courseNumberOptions: [],
      sections: [],
      error: false,
      errorType: 'negative',
      errorMessage: '',
    };
  },
  methods: {
    async loadCourseNumbers() {
      try {
        const response = await axios.get(`/api/courses`);
        this.courseNumberOptions = response.data;
        console.log(this.courseNumberOptions)
      } catch (error) {
        console.error('Error fetching course numbers:', error);
      }
    },
    async searchSections() {
      try {
        // Replace with your actual API endpoint for fetching sections
        const response = await axios.get(`/api/sections/${this.selectedDepartment}/${this.selectedCourseNumber}`);
        this.sections = response.data;
        this.error = false;
      } catch (error) {
        this.error = true;
        this.errorType = 'negative';
        this.errorMessage = 'Error fetching sections. Please try again.';
        console.error('Error fetching sections:', error);
      }
    },
  },
};
</script>

<style scoped>
.course-search {
  max-width: 400px;
  margin: auto;
  padding: 20px;
}
</style>
