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
          class="wider-dropdown q-mr-md"
          :use-input="true"
        ></q-select>

        <!-- <q-btn
          @click="searchSections"
          label="Search Sections"
          color="primary"
          class="q-ml-md, q-mr-md"
        /> -->
        <q-btn
          @click="searchSections"
          label="Search Sections"
          color="primary"
          class="q-ml-md, q-mr-md"
          :disable="!showSecondDropdown"
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

    <div
      v-if="!loading && courses.length > 0"
      class="scrollable-card-container"
    >
      <q-card
        v-for="section in courses"
        :key="section.id"
        class="scrollable-card"
      >
        <q-card-section>
          <div class="section-title">{{ section.section }}</div>
          <div>Start Time: {{ section.startTime }}</div>
          <div>End Time: {{ section.endTime }}</div>
        </q-card-section>

        <!-- Plus Button -->
        <q-card-actions>
          <q-btn
            @click="registerSection(section)"
            icon="add"
            color="primary"
            label="Add to Schedule"
          />
        </q-card-actions>
      </q-card>
    </div>
  </q-card>
</template>
<script>
import axios from "axios";

export default {
  data() {
    return {
      selectedOption1: "",
      selectedOption2: "",
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
      searchButtonDisabled: true, // New property to control the "Search Sections" button
    };
  },
  methods: {
    async loadCourseNumbers() {
      this.loading = true; // Start loading spinner
      try {
        // Fetch course numbers based on the selected department
        const response = await axios.post("/api/courses", {
          department: this.selectedOption1.value,
        });

        // Use a Set to store unique course numbers
        const uniqueCourseNumbers = new Set();

        // Iterate through the response data and add course numbers to the Set
        response.data.results.forEach((course) => {
          uniqueCourseNumbers.add(course.courseNum);
        });

        // Convert the Set to an array and assign it to dropdownOptions2
        this.dropdownOptions2 = Array.from(uniqueCourseNumbers);

        this.showSecondDropdown = true; // Show the second dropdown after loading options
        this.searchButtonDisabled = false; // Enable the "Search Sections" button
      } catch (error) {
        console.error("Error fetching course numbers:", error);
      } finally {
        this.loading = false; // Stop loading spinner
      }
    },
    async searchSections() {
      console.log("Search button clicked!");
      console.log("Selected Option 1:", this.selectedOption1);
      console.log("Selected Option 2:", this.selectedOption2);

      this.loading = true; // Start loading spinner
      try {
        // Call the API endpoint /api/sections with courseNum and courseDept parameters
        const response = await axios.post("/api/sections", {
          courseNum: this.selectedOption2,
          courseDept: this.selectedOption1.value,
        });
        console.log(response);

        // Update the 'courses' array with the response data
        this.courses = response.data.results.map((section, index) => ({
          id: index + 1, // Assuming each section has a unique identifier
          courseDept: section.courseDept,
          courseNum: section.courseNum,
          section: section.section,
          daysOfWeek: section.daysOfWeek,
          startTime: section.startTime,
          endTime: section.endTime,
          // Add more details as needed
        }));
      } catch (error) {
        console.error("Error fetching sections:", error);
      } finally {
        this.loading = false; // Stop loading spinner
      }
    },
    async registerSection(section) {
      try {
        // Replace the following line with your actual API endpoint and payload
        console.log(section.id);
        const response = await axios.post("/api/addcourse", {
          username: "dfroberg",
          courseNum: section.courseNum,
          courseDept: section.courseDept,
          section: section.section,
        });
      } catch (error) {
        console.error("Error adding course:", error);
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
.scrollable-card-container {
  max-height: 500px; /* Set the maximum height for scrollability */
  overflow-y: auto; /* Enable vertical scrolling */
}

/* Adjust styles for individual scrollable cards */
.scrollable-card {
  margin-bottom: 20px; /* Adjust margin as needed */
}
</style>
