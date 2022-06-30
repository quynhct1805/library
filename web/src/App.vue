<template>
  <v-app>
    <v-main>
      <HomePage/>
    </v-main>
  </v-app>
</template>

<script>
import HomePage from "./user/components/HomePage.vue";
// import HelloWorld from './components/HelloWorld.vue'
// import TodoList from './user/components/TodoList.vue'
// import HelloNew from './components/HelloNew.vue'

export default {
  name: 'App',

  components: {
    // HelloWorld,
    // TodoList,
    // HelloNew,
    HomePage
},

  data: () => ({
    //
  }),
}
</script>
