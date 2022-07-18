<template>
    <v-layout>
        
        <app-bar />
        <nav-bar />

        <v-main>

            <detail-book :id="id">
                Mượn
                
                <template v-slot:comment>
                    <v-banner lines="two">
                        <v-banner-avatar>
                            <v-img
                                src="/logo.jpg"
                                height="40px"
                                cover
                            ></v-img>
                        </v-banner-avatar>


                        <v-banner-text>
                            <v-textarea
                            placeholder="Viết đánh giá"
                            auto-grow
                            rows="1"
                            variant="underlined"
                            row-height="15"
                            ></v-textarea>

                            <v-rating
                                size="x-small"
                                half-increments
                                active-color="#df9e69"
                            ></v-rating>
                        </v-banner-text>

                        <v-banner-actions
                        color="#984d29">
                            <v-btn>Huy</v-btn>
                            <v-btn
                                variant="tonal"
                            >Binh luan</v-btn>
                        </v-banner-actions>
                        
                    </v-banner>
                </template>
                
            </detail-book>
        </v-main>
    </v-layout>
</template>


<script setup>
import { defineProps } from 'vue'
import AppBar from '@/components/AppBar.vue';
import NavBar from '@/components/user/NavBar.vue';
import DetailBook from '@/components/DetailBook.vue';


const props = defineProps({
    id: String
})

</script>


<style scoped>
.v-layout {
    height: 100%;
}

</style>