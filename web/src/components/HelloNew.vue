<template>
  <div>
    <h2>Filter LearnVue Articles</h2>
    <input type="text" placeholder="Filter Search" v-model="query" />
    <br/>
    <button @click="reset">Reset</button>
    <br/>
    <SearchResult :query="query" :msg="hello"/>
  </div>

</template>

<script setup>
import { ref } from 'vue'
import SearchResult from './SearchResult.vue';

const query = ref('')
const hello = ref("This is the result for search")

function reset() {
    query.value = ''
}
</script>

<style>
  input[type='text'] {
    margin-bottom: 20px;
    padding: 10px;
  }
</style>