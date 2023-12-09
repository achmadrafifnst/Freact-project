<template>
  <div class="about" style="height: 100vh;">
    <v-row height="100%" class="align-center justify-center pt-16">
      <v-col cols="12" md="6" class="py-10">
        <h1 class="text-center d-flex align-center justify-center">About</h1>
        <br>
        <v-card
          elevation="0"
          class="text-center d-flex align-center justify-center"
          style="padding-left: 25%; padding-right: 25%;"
          color="rgba(0,0,0,0)"
        >
        Freact is a web-based face forgery detection application to avoid all acts of fraud using digital face image.
        </v-card>
      </v-col>
      <v-col cols="12" md="6" class="py-10 d-flex align-center justify-center">
        <v-img class="search" src="../assets/search.png" max-width="50%" />
      </v-col>
    </v-row>
  </div>
</template>
<style scoped>
.search{
  transition-timing-function: 0.5s;
  transition-delay: 0.5s;
  transition-duration: 0.5s;
}
.search:hover{
  -webkit-transform: scaleX(-1);
  transform:scaleX(-1);
}
.about{
  background-color : rgb(0, 65, 130);
  background-image: linear-gradient(to top,rgb(0, 65, 130),grey);
}
</style>