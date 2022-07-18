<template>
    <v-layout>

        <app-bar>
            <v-btn stacked>
            <v-badge
                content="2"
                color="success"
            >
                <v-icon icon="mdi-cart"></v-icon>
            </v-badge>
        </v-btn>
        </app-bar>

        <nav-bar />

        <v-main>
            <v-chip-group
            mandatory
            column
            v-model="defaultFilteredCategory"
            >
                <router-link
                    :to="{name: 'ListBooks'}"
                >
                    <v-chip 
                        variant="outlined"
                        value="all"
                    >
                        Tất cả
                    </v-chip>
                </router-link>

                <router-link 
                    v-for="category in categories" :key="category.id"
                    :to="{name: 'ListBooks', params:{id: category.id}}"
                >
                    <v-chip 
                    variant="outlined"
                    :value="`${category.id}`"
                    >
                        {{ category.name }}
                    </v-chip>
                </router-link>
            </v-chip-group>

            <router-view :key="$route.path">
                
            </router-view>
            

        </v-main>
    </v-layout>

</template>


<script setup>
import { ref } from 'vue'
import AppBar from '../../components/AppBar.vue'
import NavBar from '@/components/user/NavBar.vue';


const categories = ref([])

const defaultFilteredCategory = ref('all')


const getCategories = async() => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    const respones = await fetch('/api/categories/')
    const result = await respones.json()
    return result
}
getCategories().then(res => categories.value = res)

</script>


<style scoped>
.v-layout {
    height: 100%;
}


/* Main */

/* ChipGroup */
.v-main ::v-deep .v-chip-group {
    margin: 16px 0 0 20px;
}

.v-chip-group ::v-deep .v-chip {
    font-size: 16px;
    padding: 12px 12px;
    margin: 8px 8px;
    color: #964a27;
}

/* Container - Search - Filter*/
.v-main ::v-deep .v-container {
    margin: 0;
    max-width: 100%;
    display: flex;
    align-items: baseline;
    padding: 8px 32px;    
}

.v-main ::v-deep .v-autocomplete {
    width: 35%;
}

.v-main ::v-deep .v-select {
    width: 15%;
    margin: 12px 0 0 24px;
}
    /* Spacer */
.v-main ::v-deep .flex-grow-1 {
    width: 50%;
}

/* List Books */
.v-main ::v-deep .v-card {
    width: 50%;
    margin: 24px auto;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    background: #f3d2b7;
}

.v-main ::v-deep .v-row {
    align-items: center;
    /* justify-content: space-evenly; */
    margin: 8px 0;
}

</style>