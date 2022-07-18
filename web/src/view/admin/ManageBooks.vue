<template>
    <v-layout>

        <app-bar />
        <nav-bar />

        <v-main>
            <v-container>
                <v-autocomplete
                    prepend-inner-icon="mdi-magnify"
                    placeholder="Nhập tên sách"
                    variant="underlined"
                    v-model="searchBook"
                    :items="books"
                    item-title="name"
                    item-value="id"
                >
                </v-autocomplete>

                <v-spacer></v-spacer>

                <v-select
                    label="Sắp xếp"
                    :items="arrange"
                    variant="underlined"
                    v-model="sort"
                ></v-select>
            </v-container>

            <v-btn
                color="success"
                dark
                @click.stop="form = true; bookInfo = Object.assign({}, {})"
            >
                Thêm
            </v-btn>


            <v-table>
                
                <v-row class="title">
                    <v-col class="text-center" cols="1">STT</v-col>
                    <v-col class="text-center">Tên sách</v-col>
                    <v-col class="text-center">Thể loại</v-col>
                    <v-col class="text-center">Tác giả</v-col>
                    <v-col class="text-center" cols="1">Phí</v-col>
                    <v-col class="text-center" cols="1">Trạng thái</v-col>
                    <v-col class="text-center">Hoạt động</v-col>
                </v-row>

                <v-row
                    class="content"
                    v-for="(book, index) in books"
                    :key="book.id"
                >
                    <router-link :to="{name: 'ManageDetailBook', params:{id: book.id}}">
                        <v-col class="text-center" cols="1">{{ (index+1) }}</v-col>
                        <v-col class="text-center">{{ book.name }}</v-col>
                        <v-col class="text-center">{{ book.category_name }}</v-col>
                        <v-col class="text-center"><span v-for="author in book.author_names" :key="author">{{ author }}<br/></span></v-col>
                        <v-col class="text-center" cols="1">{{ book.fee }}</v-col>
                        <v-col class="text-center" cols="1">{{ book.status }}</v-col>
                    </router-link>
                        <v-col class="text-center">
                            <v-btn color="warning" @click.stop="form = true; bookInfo = Object.assign({}, book)">Sửa</v-btn>
                            <v-btn color="error">Xóa</v-btn>
                        </v-col>
                </v-row>

            </v-table>

            <v-pagination
            v-model="page"
            :length="5"
            rounded="circle"
            ></v-pagination>

            <dialog-form-book 
                v-model="form"
                :form="form"
                :book="bookInfo"
                @addRespone="(res) => form = res"/>
        </v-main>
    </v-layout>

</template>


<script setup>
import { ref, watch } from 'vue'
import AppBar from '@/components/AppBar.vue';
import NavBar from '@/components/admin/NavBar.vue';
import DialogFormBook from '@/components/DialogFormBook.vue';


const page = ref(1)

const books = ref([])

const form = ref(false)
const bookInfo = ref({})

const getBooks = async() => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    const respones = await fetch('/api/admin/books/')
    const result = await respones.json()
    return result
}
getBooks().then(res => {
    books.value = res
})


const arrange = ref(['Tên sách (A-Z)', 'Trạng thái'])
const sort = ref('')

function sortBooksByName() {
    books.value.sort((a, b) => {
        if (a.name < b.name) return -1;
        if (a.name > b.name) return 1;
        return 0;
    });
}

function sortBooksByStatus() {
    books.value.sort((a, b) => {
        if (a.status === "Borrowing" & b.status === "Available") return -1;
        if (a.status === "Available" & b.status === "Borrowing") return 1;
        return 0;
    });
}

watch(sort, () => {
    if (sort.value === 'Tên sách (A-Z)') {
        sortBooksByName()
    }
    else if (sort.value === 'Trạng thái') {
        sortBooksByStatus()
    }
})



</script>


<style scoped>
.v-layout {
    height: 100%;
}


/* Main */

/* Container - Search - Filter*/

.v-main ::v-deep .v-container {
    margin: 0;
    max-width: 100%;
    display: flex;
    align-items: baseline;
    padding: 16px 32px;    
}

.v-main ::v-deep .v-autocomplete {
    width: 35%;
}

.v-main ::v-deep .v-select {
    width: 15%;
    margin: 12px 0 0 24px;
}
    
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

/* Spacer */
.v-main ::v-deep .flex-grow-1 {
    width: 50%;
}

/* Table */

.v-main ::v-deep .v-table {
    margin: 24px 8px;
    font-size: 18px;
}

/* btnAdd */
.v-main ::v-deep .v-btn {
    margin: 16px 48px;
}

/* Table */
.v-table ::v-deep .v-btn {
    margin: 0 16px 0 0;
}

.v-main ::v-deep .v-pagination {
    float: left;
}

.v-pagination ::v-deep .v-btn {
    margin: 0;
}

.v-table ::v-deep .v-row {
    margin: -8px 0;
}

.v-table ::v-deep .v-row.title {
    font-weight: bold;
    font-size: 20px;
    margin-bottom: 8px;
}

.v-row ::v-deep a {
    display: contents;
    color: black;
}

.v-table ::v-deep .v-row.content:hover {
    background-color: #F5F5F5;
}

</style>