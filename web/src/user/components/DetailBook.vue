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
                <v-list-item prepend-icon="mdi-home-outline" value="home">Trang chủ</v-list-item>
                <v-list-item prepend-icon="mdi-book-clock-outline" value="account">Đang mượn</v-list-item>
                <v-list-item prepend-icon="mdi-history" value="users">Lịch sử</v-list-item>

                <v-list-item><v-divider></v-divider></v-list-item>

                <v-list-item prepend-icon="mdi-bookmark-multiple-outline" value="rules">Nội quy</v-list-item>
                <v-list-item prepend-icon="mdi-book-open-page-variant-outline" value="intro">Giới thiệu</v-list-item>

                <v-list-item prepend-icon="mdi-cog-outline" value="intro">Cài đặt</v-list-item>
                
            </v-list>
        </v-navigation-drawer>

        <v-main>
            <v-btn
                variant="outlined"
                color="#964a27"
            >
                <v-icon
                    icon="mdi-arrow-left-thick"
                ></v-icon>
            </v-btn>

            <v-container>
                <div>
                    <v-img
                        :aspect-ratio="1"
                        src= "tatden.jpeg"
                    ></v-img>
                </div>

                <v-container>
                    <v-card>
                        <v-card-title>Số đỏ</v-card-title>
                    </v-card>

                    <v-card-content>
                        <v-card-text>Tác giả: Vũ Trọng Phụng</v-card-text>
                        <v-card-text>Thể loại: Văn học Việt Nam</v-card-text>
                        <v-card-text>Nhà xuất bản: Nhã Nam</v-card-text>
                        <v-card-text>Năm xuất bản: 2015 &emsp;&emsp;&emsp; Số trang: 200</v-card-text>
                        <v-card-text>Phí mượn: 12 &emsp;&emsp;&emsp; Hạn trả:</v-card-text>
                        <v-card-text>Tình trạng: Có sẵn</v-card-text>
                        <v-card-text>Tóm tắt: Tác phẩm kể về nhân vật chính là chị Dậu. 
                            Trước khi lấy chồng chị vốn có tên là Lê Thị Đào, một cô gái đẹp, giỏi giang, 
                            tháo vát và (theo nhà văn) sinh ra trong gia đình trung lưu. 
                        </v-card-text>
                    </v-card-content>

                    <v-btn
                        color="success"
                        flat
                    >
                        Mượn
                    </v-btn>
                </v-container>
            </v-container>
        </v-main>
    </v-layout>
</template>


<script setup>
import { ref } from 'vue'
// import { useRoute } from "vue-router"
const hideNav = ref(true)

// const getBook = async(book_id) => {
//     const myHeaders = new Headers();
//     myHeaders.append('Content-Type', 'application/json');

//     const respones = await fetch(`/api/books/${book_id}`)
// }


// const getBooks = async() => {
//     const myHeaders = new Headers();
//     myHeaders.append('Content-Type', 'application/json');
//     const respones = await fetch('/api/books/')
//     const result = await respones.json()
//     return result
// }
// getBooks().then(res => books.value = res)
// books.value = getBooks()
// onMounted(async () => {books.value = await getBooks()})

// const route = useRoute();
// const id = route.params.id;
// console.log(id)

</script>


<style scoped>
.v-layout {
    height: 100%;
}

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

.v-main ::v-deep .v-btn {
    border-radius: 15px;
    min-width: 56px;
    font-size: 1rem;
    margin: 32px 0 0 40px;
}

.v-main ::v-deep .v-container {
    margin: 0;
    max-width: 100%;
    display: flex;
    padding-top: 70px;
}

.v-container ::v-deep .v-img {
    width: 400px;
    margin: 0 70px;
}

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
    padding: 8px 16px;
    font-size: 20px;
}

.v-container ::v-deep .v-btn {
    height: 40px;
    border-radius: 4px;
}
</style>