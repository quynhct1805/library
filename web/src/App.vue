<template>
  <v-app>
    <v-main>
      <TodoList/>
    </v-main>
  </v-app>
</template>

<script>
// import HelloWorld from './components/HelloWorld.vue'
import TodoList from './components/TodoList.vue'
// import HelloNew from './components/HelloNew.vue'

export default {
  name: 'App',

  components: {
    // HelloWorld,
    TodoList,
    // HelloNew
},

  data: () => ({
    //
  }),
}
</script>
