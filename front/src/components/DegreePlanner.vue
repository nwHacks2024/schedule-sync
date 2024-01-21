<template>
  <h2>UBC Computer Science Requirements</h2>
  <div>
    <q-page>
      <q-row>
        <q-col v-for="level in levels" :key="level" :span="12 / levels.length" class="row">
          <h3>Year {{ level }}</h3>
          <div class="course-list">
            <div v-for="course in filteredCourses(level)" :key="course.code" class="course-item">
              {{ course.code }}{{ course.number }}
            </div>
          </div>
        </q-col>
      </q-row>
    </q-page>
  </div>
</template>

<style scoped>
div {
  font-family: 'Helvetica', sans-serif;
}
.course-list {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}

h3{
  padding-right:40px;
}

.course-item {
  margin-right: 10px;
  margin-bottom: 25px;
  padding: 8px;
  padding-top:50px;
  border: 2px solid #838383;
  border-radius: 8px;
  background-color: #f6f6f6;
  transition: border-color 0.3s ease-in-out, background-color 0.3s ease-in-out;
}

.course-item:hover {
  background-color: #e5e5e5; /* Change to your desired hover background color */
}

</style>

<script>
export default {
  data() {
    return {
      courses: [
        { code: 'CPSC ', number: '110' },
        { code: 'CPSC ', number: '121' },
        { code: 'CPSC ', number: '210' },
        { code: 'CPSC ', number: '213' },
        { code: 'CPSC ', number: '221' },
        { code: 'CPSC ', number: '313' },
        { code: 'CPSC ', number: '320' },
        { code: 'CPSC ', number: '310' },
        { code: 'CPSC ', number: '3xx' },
        { code: 'CPSC ', number: '3xx' },
        { code: 'CPSC ', number: '3xx' },
        { code: 'CPSC ', number: '4xx' },
        { code: 'CPSC ', number: '4xx' },
        { code: 'CPSC ', number: '4xx' },
        { code: 'MATH ', number: '100' },
        { code: 'MATH ', number: '101' },
        { code: 'MATH ', number: '200' },
        { code: 'MATH ', number: '221' },
        { code: 'STAT ', number: '251' },
        // Add more courses as needed
      ],
      levels: [1, 2, 3, 4],
    };
  },
  methods: {
    filteredCourses(level) {
      return this.courses.filter(course => course.code && course.number && course.number.startsWith(level));
    },
    toggleSelection(course) {
      const index = this.selectedCourses.indexOf(course);
      if (index === -1) {
        this.selectedCourses.push(course);
      } else {
        this.selectedCourses.splice(index, 1);
      }
    },
  },
};
</script>
