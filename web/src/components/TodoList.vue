<template>
    <v-container>
        <v-btn
            variant="outlined"
            icon="mdi-plus"
            color="primary"
            size="x-small"
            @click="addTodo"
        ></v-btn>

        <v-list>
            <v-list-item
                v-for="todo in todos"
                :key="todo.id"
                active-color="primary"
                variant="elevated"
            >
                <v-checkbox></v-checkbox>
                <v-text-field v-model="todo.text"></v-text-field>
                <v-btn
                    icon="mdi-delete"
                    size="x-small"
                    @click="removeTodo(todo)"
                ></v-btn>
            </v-list-item>
        </v-list>

    </v-container>
</template>

<script setup>
import { ref } from 'vue'

let id = 0
const todos = ref([
    { id: id++, text: 'Add Todo Items' },
    { id: id++, text: 'Star Items' },
    { id: id++, text: 'Filter Items' },
])

function addTodo() {
    todos.value.push({id: id++, text: ''})
}

function removeTodo(todo) {
    todos.value = todos.value.filter((t) => t !== todo)
}

</script>

<style scoped>
.v-list-item ::v-deep .v-checkbox {
    flex: none;
}
.v-input ::v-deep .v-input__details {
    display: none;
}
.v-list-item ::v-deep .v-field__field,
.v-list-item ::v-deep .v-field__input {
    padding-top: 0px;
    padding-bottom: 0;
}
.v-list-item ::v-deep .v-btn {
    margin-left: 10px;
}
.v-list-item ::v-deep .v-field__input,
.v-list-item ::v-deep .v-checkbox,
.v-list-item ::v-deep .v-btn{
    color: red;
}
</style>