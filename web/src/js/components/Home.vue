<template>
    <div class="container-margin-top">
        <div class="row">
            <div class="col-sm-12 text-center">
                <h1>Home</h1>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-12 text-center">
                <h2>{{ this.$store.state.msg }}</h2>
            </div>
        </div>
        <div class="row">
            <div class="col-sm-12 text-center margin-top">
                <router-link :to="{ name: 'garages' }" tag="a" class="btn btn-primary">Garages</router-link>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Home"
    }
</script>

<style scoped></style>