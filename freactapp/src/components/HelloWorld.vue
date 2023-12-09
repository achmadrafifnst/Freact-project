<template>
    <div>
    <v-row class="text-center justify-center" >
      <v-card 
        width = 100%
        height = 100vh
        class = "d-flex align-center justify-center"
        id="home"
      >
        <v-col class="align-center justify-center" style="margin-top: -50px;">
          <h1 class="display-2 font-weight-bold mb-3">
            <p style="color:rgb(228, 113, 36); font-size: 250%;"  id="app-name">Freact</p>
          </h1>

          <v-btn class="mt-10 pa-6" style="font-size: 20px; color: white; background-color:rgb(228, 113, 36) ;">
            Start
          </v-btn>
        </v-col>
      </v-card>

      
    </v-row>
    <v-row id="about" height="100%" class="align-center justify-center pt-16">
      <v-col cols="12" md="6" class="py-10">
        <h1 class="text-center align-center justify-center">About</h1>
        <br>
        <v-card
          elevation="0"
          class="text-center align-center justify-center"
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

<script>
  export default {
    name: 'HelloWorld',
    data: () => ({
      ecosystem: [
        {
          text: 'vuetify-loader',
          href: 'https://github.com/vuetifyjs/vuetify-loader',
        },
        {
          text: 'github',
          href: 'https://github.com/vuetifyjs/vuetify',
        },
        {
          text: 'awesome-vuetify',
          href: 'https://github.com/vuetifyjs/awesome-vuetify',
        },
      ],
      importantLinks: [
        {
          text: 'Documentation',
          href: 'https://vuetifyjs.com',
        },
        {
          text: 'Chat',
          href: 'https://community.vuetifyjs.com',
        },
        {
          text: 'Made with Vuetify',
          href: 'https://madewithvuejs.com/vuetify',
        },
        {
          text: 'Twitter',
          href: 'https://twitter.com/vuetifyjs',
        },
        {
          text: 'Articles',
          href: 'https://medium.com/vuetify',
        },
      ],
      whatsNext: [
        {
          text: 'Explore components',
          href: 'https://vuetifyjs.com/components/api-explorer',
        },
        {
          text: 'Select a layout',
          href: 'https://vuetifyjs.com/getting-started/pre-made-layouts',
        },
        {
          text: 'Frequently Asked Questions',
          href: 'https://vuetifyjs.com/getting-started/frequently-asked-questions',
        },
      ],
    }),
  }
</script>
<style scoped>
#home{
  background: url('../assets/latar2.jpg') center center;
  height: 100vh;
}
.search{
  transition-timing-function: 0.5s;
  transition-delay: 0.5s;
  transition-duration: 0.5s;
}
.search:hover{
  -webkit-transform: scaleX(-1);
  transform:scaleX(-1);
}
#about{
  background-color : rgb(0, 65, 130);
  background-image: linear-gradient(to top,rgb(0, 65, 130),grey);
  height: 100vh;
}
@media screen and (max-width:600px) {
  #app-name{
    font-size: 200%;
  }
}
</style>
