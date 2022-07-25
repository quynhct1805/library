<template>

    <v-card>
        <v-card-title>
            <span class="text-h5">Thêm thể loại</span>
        </v-card-title>
        <v-card-text>
            <v-container>
                <v-row>
                    <v-col
                        cols="12"
                    >
                        <v-text-field
                        label="Mã thể loại"
                        persistent-hint
                        variant="underlined"
                        v-model="cate.code"
                        ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                    >
                        <v-text-field
                        label="Tên thể loại"
                        placeholder=""
                        clearable
                        variant="underlined"
                        v-model="cate.name"
                        ></v-text-field>
                    </v-col>
                    <v-col
                        cols="12"
                    >
                        <v-textarea
                        label="Mô tả"
                        placeholder=""
                        clearable
                        variant="underlined"
                        v-model="cate.description"
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
                @click='emit("addRespone", false)'
            >
                Hủy
            </v-btn>
            <v-btn
                color="#62311a"
                text
                @click="handledClickSave"
            >
                Lưu
            </v-btn>
        </v-card-actions>
    </v-card>

</template>


<script setup>
import { defineProps, defineEmits, reactive } from 'vue'

const props = defineProps({
    category: Object,
    action: String
})


const cate = reactive({...props.category})

const emit = defineEmits(['addRespone'])


const createCategory = () => {
    fetch('/api/categories/',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },

            body: JSON.stringify({
                ...cate
            })
        }
    )
}


const updateCategory = () => {
    fetch(`/api/categories/${cate.id}`,
        {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                ...cate
            })
        }
    )
}



function handledClickSave() {

    if (props.action === 'add') 
        createCategory()
    else 
        updateCategory()

    emit("addRespone", false)
}

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