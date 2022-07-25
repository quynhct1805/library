<template>
    <v-layout>
        
        <app-bar />
        <nav-bar />

        <v-main>
            <v-container>
                <v-autocomplete
                    prepend-inner-icon="mdi-magnify"
                    placeholder="Nhập tên thể loại"
                    variant="underlined"
                    v-model="searchCategory"
                    :items="categories"
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

            
            <v-btn
                color="success"
                @click.stop="form = true; categoryInfo = Object.assign({}, {}), action = 'add'"
            >
                Thêm
            </v-btn>

            <v-table>
                
                <v-row class="title">
                    <v-col class="text-center" cols="1">STT</v-col>
                    <v-col class="text-center" cols="1">Mã loại</v-col>
                    <v-col class="text-center">Tên loại</v-col>
                    <v-col class="text-center">Mô tả</v-col>
                    <v-col class="text-center" cols="2">Hoạt động</v-col>
                </v-row>

                <v-row
                    v-for="(category, index) in categories"
                    :key="category.id"
                    class="content"
                >
                    <v-col class="text-center" cols="1">{{ (index+1) }}</v-col>
                    <v-col class="text-center" cols="1">{{ category.code }}</v-col>
                    <v-col class="text-center">{{ category.name }}</v-col>
                    <v-col class="text-center">{{ category.description }}</v-col>
                    <v-col class="text-center" cols="2">
                        <v-btn color="warning" @click.stop="form = true; categoryInfo = Object.assign({}, category), action='edit'">
                        Sửa</v-btn>
                        <v-btn color="error">Xóa</v-btn>
                    </v-col>

                </v-row>

            </v-table>

            <v-pagination
            v-model="page"
            :length="5"
            rounded="circle"
            ></v-pagination>

            <v-dialog
            v-model="form"
            persistent
            >
                <dialog-form-category 
                    :category="categoryInfo"
                    :action="action"
                    @addRespone="(res) => form = res"/>
            </v-dialog>
        </v-main>
    </v-layout>

</template>


<script setup>
import { ref, watch } from 'vue'
import AppBar from '@/components/AppBar.vue';
import NavBar from '@/components/admin/NavBar.vue';
import DialogFormCategory from '@/components/DialogFormCategory.vue';

const categories = ref([])
const categoryInfo = ref({})
const action = ref('')

const form = ref(false)

const getCategories = async() => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    const respones = await fetch('/api/categories/')
    const result = await respones.json()
    return result
}
getCategories().then(res => categories.value = res)


const arrange = ref(['Tên loại (A-Z)'])
const sort = ref('')

function sortCategoriesByName() {
    categories.value.sort((a, b) => {
        if (a.name < b.name) return -1;
        if (a.name > b.name) return 1;
        return 0;
    });
}

watch(sort, () => {
    if (sort.value === 'Tên loại (A-Z)') {
        sortCategoriesByName()
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