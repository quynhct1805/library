<template>

    <v-dialog
    v-model="form"
    persistent
    >
        <v-card>
            <v-card-title>
                <span class="text-h5">Thêm sách</span>
            </v-card-title>
            <v-card-text>
                <v-container>
                    <v-row>
                        <v-col
                            cols="12"
                        >
                            <v-file-input
                                multiple
                                label="Hình ảnh"
                                variant="underlined"
                            ></v-file-input>
                        </v-col>
                        <v-col
                            cols="12"
                        >
                            <v-text-field
                            label="Tên sách"
                            placeholder=""
                            clearable
                            variant="underlined"
                            v-model="book.name"
                            ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                        >
                            <v-text-field
                            label="Nhà xuất bản"
                            persistent-hint
                            variant="underlined"
                            v-model="book.publisher"
                            ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            md="8"
                        >
                            <v-autocomplete
                                v-model="book.author_names"
                                :items="authors"
                                item-title="name"
                                item-value="id"
                                label="Tác giả"
                                variant="underlined"
                                multiple
                            ></v-autocomplete>
                        </v-col>
                        <v-col
                            cols="12"
                            md="4"
                        >
                            <v-autocomplete
                                v-model="book.category_name"
                                :items="categories"
                                item-title="name"
                                item-value="id"
                                label="Thể loại"
                                variant="underlined"
                            ></v-autocomplete>
                        </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                            <v-text-field
                            label="Năm xuất bản"
                            persistent-hint
                            variant="underlined"
                            v-model="book.year"
                            ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                            <v-text-field
                            label="Số trang"
                            persistent-hint
                            variant="underlined"
                            v-model="book.pages"
                            ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                            <v-text-field
                            label="Phí"
                            persistent-hint
                            variant="underlined"
                            v-model="book.fee"
                            ></v-text-field>
                        </v-col>
                        <v-col
                            cols="12"
                        >
                            <v-textarea
                            label="Tóm tắt"
                            variant="underlined"
                            v-model="book.summary"
                            ></v-textarea>
                        </v-col>
                    </v-row>
                </v-container>
            </v-card-text>

            <v-card-actions>
                <v-spacer></v-spacer>
                <v-btn
                    color="blue darken-4"
                    text
                    @click="form = false"
                >
                    Hủy
                </v-btn>
                <v-btn
                    color="#62311a"
                    text
                    @click="form = false"
                >
                    Lưu
                </v-btn>
            </v-card-actions>
        </v-card>
    </v-dialog>

</template>


<script setup>
import { ref, defineProps, defineEmits, reactive, computed } from 'vue'

const props = defineProps({
    form: Boolean,
    book: Object
})

const form = ref(props.form)
const bookss = computed(() => props.book)

const emit = defineEmits(['addRespone'])

emit('addRespone', form)


const authors = ref([])
const getAuthors = async() => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    const respones = await fetch('/api/authors/')
    const result = await respones.json()
    return result
}
getAuthors().then(res => {
    authors.value = res
})


const categories = ref([])
const getCategories = async() => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    const respones = await fetch('/api/categories/')
    const result = await respones.json()
    return result
}
getCategories().then(res => {
    categories.value = res
})


</script>


<style scoped>
.v-dialog {
    max-width: 800px;
}

.v-autocomplete ::v-deep input {
    width: 100%;
}

.v-autocomplete ::v-deep .v-field__input {
    height: 24px;
}
</style>