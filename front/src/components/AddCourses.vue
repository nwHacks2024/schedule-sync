<template>
  <q-card class="my-card">
    <q-card-section>
      <div class="header-container">
        <q-select
          v-model="selectedOption1"
          :options="dropdownOptions1"
          label="Course Department"
          class="wider-dropdown q-mr-md"
        ></q-select>
        <q-btn
          @click="loadCourseNumbers"
          label="Load Course Numbers"
          color="primary"
          class="q-ml-md, q-mr-md"
        />

        <q-select
          v-if="showSecondDropdown"
          v-model="selectedOption2"
          :options="dropdownOptions2"
          label="Course Number"
          class="wider-dropdown"
        ></q-select>

        <q-btn
          @click="searchSections"
          label="Search Sections"
          color="primary"
          class="q-ml-md, q-mr-md"
        />
      </div>
    </q-card-section>

    <!-- Loading Spinner -->
    <q-spinner
      v-if="loading"
      size="50px"
      color="primary"
      class="q-mt-md, q-mr-md"
    />

    <!-- Card Carousel -->
    <q-carousel
      v-if="!loading && courses.length > 0"
      control-color="primary"
      arrows
      navigation
      infinite
      class="q-mt-md"
    >
      <q-card v-for="course in courses" :key="course.id">
        <q-card-section>
          <!-- <q-card-title>{{ course.title }}</q-card-title> -->
        </q-card-section>
        <q-card-section>
          <p>{{ course.description }}</p>
        </q-card-section>
        <!-- Add more card content as needed -->
      </q-card>
    </q-carousel>
  </q-card>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      selectedOption1: null,
      selectedOption2: null,
      dropdownOptions1: [
        { label: "CPSC", value: "CPSC" },
        { label: "MATH", value: "MATH" },
        { label: "STAT", value: "STAT" },
        // Add more options as needed
      ],
      dropdownOptions2: [],
      courses: [], // Add your course data here
      loading: false, // Indicates whether an API call is in progress
      showSecondDropdown: false, // Flag to control the visibility of the second dropdown
    };
  },
  methods: {
    async loadCourseNumbers() {
      console.log("Loading Courses");
      console.log("Selected Department:", this.selectedOption1);

      this.loading = true; // Start loading spinner
      try {
        // Fetch course numbers based on the selected department
        const response = await axios.post("/api/courses", {
          department: this.selectedOption1.value,
        });
        console.log("Response:", response.data);

        // Use a Set to store unique course numbers
        const uniqueCourseNumbers = new Set();

        // Iterate through the response data and add course numbers to the Set
        response.data.results.forEach(course => {
          uniqueCourseNumbers.add(course.courseNum);
        });

        // Convert the Set to an array and assign it to dropdownOptions2
        this.dropdownOptions2 = Array.from(uniqueCourseNumbers);

        this.showSecondDropdown = true; // Show the second dropdown after loading options
      } catch (error) {
        console.error("Error fetching course numbers:", error);
      } finally {
        this.loading = false; // Stop loading spinner
      }
    },
    async searchSections() {
      // Add your search logic here
      console.log("Search button clicked!");
      console.log("Selected Option 1:", this.selectedOption1);
      console.log("Selected Option 2:", this.selectedOption2);

      this.loading = true; // Start loading spinner
      try {
        // Fetch courses based on selected options and update the 'courses' array
        // Replace the following line with your actual API call or data retrieval logic
        this.courses = [
          { id: 1, title: "Course 1", description: "Description for Course 1" },
          { id: 2, title: "Course 2", description: "Description for Course 2" },
          // Add more courses as needed
        ];
      } catch (error) {
        console.error("Error fetching courses:", error);
      } finally {
        this.loading = false; // Stop loading spinner
      }
    },
  },
};
</script>




<style scoped>
.my-card {
  max-width: 800px; /* Adjust the max-width as needed */
  margin: auto;
  margin-top: 20px;
  padding: 20px;
}

.header-container {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.wider-dropdown {
  min-width: 200px; /* Adjust the min-width as needed */
}

/* Add margin to the right of the first q-select */
.q-mr-md {
  margin-right: 10px; /* Adjust the margin as needed */
}
</style>
