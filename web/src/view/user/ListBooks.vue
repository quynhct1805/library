<template>

        <v-container>
            <v-autocomplete
                prepend-inner-icon="mdi-magnify"
                placeholder="Nhập tên sách"
                variant="underlined"
                v-model="searchBook"
                :items="books"
                item-title="name"
                item-value="id"
            ></v-autocomplete>

            <v-spacer></v-spacer>

            <v-select
                label="Sắp xếp"
                :items="arrange"
                variant="underlined"
                v-model="sort"
            ></v-select>
        </v-container>

        <v-card>{{ categories.name }}</v-card>

        
        <v-row>
            <div v-for="book in books" :key="book.id">
                <v-col>
                    <router-link :to="{name: 'DetailBook', params:{id: book.id}}">
                        <v-img
                            width="300"
                            :aspect-ratio="1"
                            :src= "`/${book.image}`"
                        
                        ></v-img>
                        <v-card-title class="justify-center">
                            {{ book.name }}
                        </v-card-title>
                    </router-link>
                </v-col>
            </div>
        </v-row>
    
</template>

<script setup>
import { ref, defineProps, computed, watch } from 'vue'

const props = defineProps({
    category_id: {type: String, default: ''},
})

const books = ref([])
const getBooksByCategory = async() => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    const respones = await fetch(`/api/books/${props.category_id}`)
    const result = await respones.json()
    return result
}
getBooksByCategory().then(res => books.value = res)


const categories = ref({})
const getCategory = async() => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    const respones = await fetch(`/api/categories/${props.category_id}`)
    const result = await respones.json()
    return result
}
getCategory().then(res => categories.value = res)


const result = computed(() => {
    const reducer = (mapBook, book) => {
        const bookInfo = {id: book.id, name: book.name}
        if( mapBook[book.category_id] ) {
            mapBook[book.category_id].push(bookInfo)
        } else {
            mapBook[book.category_id] = [bookInfo]
        }
        return mapBook
    }

    return books.value.reduce(reducer, {})
})

// console.log(result)


const arrange = ref(['Tên sách (A-Z)', 'Đánh giá', 'Số lượt mượn'])
const sort = ref('')

function sortBooksByName() {
    books.value.sort((a, b) => {
        if (a.name < b.name) return -1;
        if (a.name > b.name) return 1;
        return 0;
    });
}

function sortBooksByNumBorrow() {
    books.value.sort((a, b) => {
        return b.number_borrow - a.number_borrow;
    })
}

function sortBooksByReview() {
    books.value.sort((a, b) => {
        return b.reviews - a.reviews;
    })
}

watch(sort, () => {
    if (sort.value === 'Tên sách (A-Z)') {
        sortBooksByName()
    }
    else if (sort.value === 'Số lượt mượn') {
        sortBooksByNumBorrow()
    }
    else if (sort.value === 'Đánh giá') {
        sortBooksByReview()
    }
})
</script>


<style scoped>
/* Container - Search - Filter*/

.v-autocomplete ::v-deep .v-field__field {
    padding-top: 6px;
}

.v-autocomplete ::v-deep .v-field__prepend-inner {
    padding: 8px 4px;
}

.v-autocomplete ::v-deep .v-input__details,
.v-select ::v-deep .v-input__details {
    display: none;
}

.v-autocomplete ::v-deep input {
    width: 100%;
}


/* List Books */

.v-row ::v-deep div {
    width: 25%;
    min-width: 340px;
}

.v-row ::v-deep .v-col {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    margin-top: 16px;
    width: 100%;
}

.v-col ::v-deep .v-card-title {
    margin-top: 8px;
    font-size: 24px;
    width: auto;
}

.v-col ::v-deep a {
    text-decoration: none;
    color: black;
}
</style>
