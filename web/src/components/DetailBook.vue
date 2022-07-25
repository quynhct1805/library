<template>
    <v-btn
        variant="outlined"
        color="#964a27"
        @click="router.back()"
    >
        <v-icon
            icon="mdi-arrow-left-thick"
        ></v-icon>
    </v-btn>

    <v-container>
        <div class="img">
            <v-img
                :aspect-ratio="1"
                :src= "`/${book.image}`"
            ></v-img>
        </div>

        <v-container>
            <v-card>
                <v-card-title>{{book.name}}</v-card-title>
            </v-card>

            <v-card-content>
                <v-card-text>Tác giả: <span v-for="author in authors" :key="author.id">{{author.name}}&emsp;</span></v-card-text>
                <v-card-text>Thể loại: {{book.category_name}}</v-card-text>
                <v-card-text>Nhà xuất bản: {{book.publisher}}</v-card-text>
                <v-row>
                    <v-col><v-card-text>Năm xuất bản: {{book.year}}</v-card-text><v-card-text>Phí mượn: {{book.fee}}</v-card-text></v-col>
                    <v-col><v-card-text>Số trang: {{book.pages}}</v-card-text><v-card-text>Hạn trả:{{book.due_date}}</v-card-text></v-col>
                </v-row>
                <v-card-text>Tình trạng: {{book.status}}</v-card-text>
                <v-card-text>Người mượn: {{userBorrow.user}}</v-card-text>
                <v-card-text>Tóm tắt: {{book.summary}}</v-card-text>
            </v-card-content>

            <v-btn
                color="success"
                flat
                @click="updatedStatus()"
                :disabled="isDisable[book.status]"
            >
                <slot></slot>
            </v-btn>
        </v-container>
    </v-container>

    <v-container class="comment">
        <div>
            <p>Lượt mượn: {{book.number_borrow}}</p>
            <p>
                Đánh giá: 
                <strong>{{book.reviews}}</strong><v-icon icon="mdi-star" size="x-small"></v-icon>
            </p>
        </div>
        <v-list>
            Bình luận

            <slot name="comment"></slot>

            <v-list-item v-for="comment in comments" :key="comment">
                
                <div>
                    <h5>{{comment.user}} 
                        <span class="time">{{comment.created_at}}</span>
                    </h5> 
                    <v-rating
                        size="x-small"
                        half-increments
                        v-model="comment.rate"
                        active-color="#df9e69"
                        readonly
                    ></v-rating>
                    <v-card-text>{{comment.cmt}}</v-card-text>
                </div>
                
            </v-list-item>
        </v-list>
    </v-container>
</template>


<script setup>
import { ref, defineProps } from 'vue'
import { useRouter } from "vue-router"

const props = defineProps({
    id: String
})

const isDisable = ref({'Available': true, 'Borrowing': false})
const router = useRouter();

const book = ref([])
const getBook = async() => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    const respones = await fetch(`/api/book/${props.id}`)
    const result = await respones.json()
    return result
}
getBook().then(res => book.value = res)


const authors = ref([])
const getAuthors = async() => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    const respones = await fetch(`/api/author/${props.id}`)
    const result = await respones.json()
    return result
}
getAuthors().then(res => authors.value = res)


const updatedStatus = async() => {
    await fetch(`/api/book/${props.id}`, 
    {method: 'PATCH',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
        }}
    )
    // const result = await respones.json()
}


const userBorrow = ref({})
const getUserBorrow = async() => {
    const myHeaders = new Headers();
    myHeaders.append('Content-Type', 'application/json');
    const respones = await fetch(`/api/user_borrow/${props.id}`)
    const result = await respones.json()
    return result
}
getUserBorrow().then(res => userBorrow.value = res)


const comments = ref([])
const getReviewsBook = async() => {
    const myHeaders = new Headers()
    myHeaders.append('Content-Type', 'application/json')
    const respones = await fetch(`/api/reviews_book/${props.id}`)
    const result = await respones.json()
    return result
}
getReviewsBook().then(res => comments.value = res)


</script>


<style scoped>
.v-layout {
    height: 100%;
}

/* Main */

/* btnBack */
.v-btn {
    border-radius: 15px;
    min-width: 56px;
    font-size: 1rem;
    margin: 32px 0 0 40px;
}


/* Container */
.v-container {
    margin: 0;
    max-width: 100%;
    display: flex;
    padding-top: 70px;
}

/* Img */
.v-container ::v-deep div.img {
    width: 40%;
}

.v-container ::v-deep .v-img {
    width: 100%;
    padding: 0 40px;
}

/* Container Info */
.v-container ::v-deep .v-container {
    display: block;
    padding-top: 0;
    width: 50%;
    margin-left: 50px;
    margin-right: auto;
}

.v-container ::v-deep .v-card {
    max-width: 100%;
    background-color: #f0e2ca;
}

.v-card ::v-deep .v-card-title {
    text-align: center;
    text-transform: uppercase;
    display: block;
    font-size: 32px;
}

.v-card-content ::v-deep .v-card-text {
    padding: 12px 16px;
    font-size: 20px;
}

.v-container ::v-deep .v-btn {
    height: 40px;
    border-radius: 4px;
}





/* Container comment */
.v-container.comment {
    font-size: 24px;
    padding: 18px 15%;
    display: block;
}


p ::v-deep strong {
    font-size: 36px;
}

.v-list-item ::v-deep span.time {
    font-size: 16px;
    color: gray;
    font-style: oblique;
    font-weight: 400;
}

.v-rating ::v-deep .v-btn {
    margin: 0px;
    min-width: 20px;
    height: 20px;
}

.v-list-item ::v-deep .v-card-text {
    padding: 0;
    font-size: 1.1rem;
}


.v-list ::v-deep .v-input__details {
    display: none;
}

.v-banner-actions ::v-deep .v-btn {
    margin: 0;
}
</style>