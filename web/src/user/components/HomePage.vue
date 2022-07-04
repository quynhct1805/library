<template>
    <v-layout>
        <v-app-bar
        color="#e4bb9a"
        prominent
        >
            <v-app-bar-nav-icon variant="text" @click.stop="hideNav = !hideNav"></v-app-bar-nav-icon>

            <v-toolbar-title>
                <v-avatar>
                    <v-img
                        :src="require('../assets/logo.jpg')"
                        height="40px"
                        cover
                    ></v-img>
                </v-avatar>
                Thư viện
            </v-toolbar-title>

            <v-btn stacked>
                <v-badge
                    content="2"
                    color="success"
                >
                    <v-icon icon="mdi-cart"></v-icon>
                </v-badge>
            </v-btn>

            <v-btn variant="text" icon="mdi-account-circle"></v-btn>
        </v-app-bar>

        <v-navigation-drawer
        permanent
        location="left"
        v-model="hideNav"
        >
            <v-divider></v-divider>

            <v-list density="compact" nav>
                <v-list-item prepend-icon="mdi-home-outline" value="home" href="http://localhost:3000/">Trang chủ</v-list-item>
                <v-list-item prepend-icon="mdi-book-clock-outline" value="account">Đang mượn</v-list-item>
                <v-list-item prepend-icon="mdi-history" value="users">Lịch sử</v-list-item>

                <v-list-item><v-divider></v-divider></v-list-item>

                <v-list-item prepend-icon="mdi-bookmark-multiple-outline" value="rules">Nội quy</v-list-item>
                <v-list-item prepend-icon="mdi-book-open-page-variant-outline" value="intro">Giới thiệu</v-list-item>

                <v-list-item prepend-icon="mdi-cog-outline" value="intro">Cài đặt</v-list-item>
                
            </v-list>
        </v-navigation-drawer>

        <v-main>
            <v-chip-group
            mandatory
            column
            v-model="defaultFilteredBooks"
            >
                <v-chip 
                    variant="outlined"
                    @click="filteredGetAllBooks()"
                    value="all"
                >
                    Tất cả
                </v-chip>
                <v-chip 
                variant="outlined"
                v-for="category in categories" :key="category.id"
                @click="filteredByCategoryId(category.id)"
                >
                    {{ category.name }}
                </v-chip>
            </v-chip-group>

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
                    
                ></v-select>
            </v-container>

            <div 
                v-for="category in categories" :key="category.id"
            >
                <v-card>{{ category.name }}</v-card>
    
                <v-row>
                    <div v-for="book in filteredBooks" :key="book.id">
                        <v-col v-if="book.category_id === category.id">
                            <v-img
                                width="300"
                                :aspect-ratio="1"
                                :src= "`/${book.image}`"
                            ></v-img>
                            <v-card-title >
                                {{ book.name }}
                            </v-card-title>
                        </v-col>
                    </div>
                </v-row>
            </div>

        </v-main>
    </v-layout>

</template>


<script setup>
import { onMounted, ref, computed } from 'vue'
const hideNav = ref(true)

const categories = ref([])

const arrange = ref(['Tên sách (A-Z)', 'Đánh giá', 'Số lượt mượn'])
const sort = ref('')

const books = ref([])
const filteredBooks = ref([])
const defaultFilteredBooks = ref('all')

const searchBook = null

const getCategories = async() => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    const respones = await fetch('/api/categories/')
    const result = await respones.json()
    return result
}
getCategories().then(res => categories.value = res)



const getBooks = async() => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    const respones = await fetch('/api/books/')
    const result = await respones.json()
    return result
}
getBooks().then(res => {
    books.value = res
    filteredBooks.value = res
})


function filteredByCategoryId(category_id) {
    filteredBooks.value = books.value.filter((b) => b.category_id === category_id)
}

function filteredGetAllBooks() {
    filteredBooks.value = books.value
}

function sortBooks() {
    filteredBooks.value.sort((a, b) => {
        const nameA = a.name; 
        const nameB = b.name; 
        if (nameA < nameB) return -1;
        if (nameA > nameB) return 1;

        return 0;
    });
}


</script>


<style scoped>
/* NavBar */
.v-list ::v-deep .v-list-item--nav:not(:only-child) {
    height: 50px;
    font-size: 24px;
    padding-left: 16px;
    margin-bottom: 8px;
}

.v-list-item ::v-deep .v-icon {
    margin-right: 16px;
}


/* ToolBar */
.v-toolbar ::v-deep .v-toolbar-title {
    font-size: 28px;
    text-transform: uppercase;
    margin-left: 8px;
    line-height: 44px;
}

.v-toolbar-title ::v-deep .v-avatar {
    margin-right: 8px;
    margin-top: -4px;
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
/* .v-container ::v-deep .v-container {
    width: 35%;
    padding: 8px 0;
    display: block;
} */

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
    justify-content: space-evenly;
    margin: 8px 0;
}

.v-row ::v-deep .v-col {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    margin-top: 12px;
}

.v-col ::v-deep .v-card-title {
    margin-top: 8px;
    font-size: 24px;
}
</style>