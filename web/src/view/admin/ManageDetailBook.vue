<template>
    <v-layout>

        <app-bar />
        <nav-bar />

        <v-main>

            <detail-book :id="id">Trả</detail-book>
        </v-main>
    </v-layout>
</template>


<script setup>
import { defineProps } from 'vue'
import AppBar from '@/components/AppBar.vue';
import NavBar from '@/components/admin/NavBar.vue';
import DetailBook from '@/components/DetailBook.vue';

defineProps({
    id: String
})


</script>


<style scoped>
.v-layout {
    height: 100%;
}

</style>