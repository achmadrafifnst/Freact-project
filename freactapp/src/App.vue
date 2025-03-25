<template>
  <v-app elevate-on-scroll  class="app">
    <v-app-bar
      app
      color="#18348B"
      dark
      class="px-2"
      fixed
    >
      <div class="d-flex align-center">
        <!-- <v-img
          alt="Vuetify Logo"
          class="shrink mr-2"
          contain
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-logo-dark.png"
          transition="scale-transition"
          width="40"
        /> -->
        <v-img 
          src="./assets/logo.png" 
          width="40"
          transition="scale-transition"  
        />
        <!-- <v-img
          alt="Vuetify Name"
          class="shrink mt-1 hidden-sm-and-down"
          contain
          min-width="100"
          src="https://cdn.vuetifyjs.com/images/logos/vuetify-name-dark.png"
          width="100"
        /> -->
      </div>

      <v-spacer></v-spacer>

      <v-btn
        href="#home"
        text
        class="hidden-sm-and-down"
        @click="onClickMenu"
      >
        <span class="ma-0">Home</span>
      </v-btn>
      
      <v-btn
        href="https://achmadrafifnasution.vercel.app/contact"
        text
        class="hidden-sm-and-down"
      >
        <span class="ma-0">Contact Me</span>
      </v-btn>

      <v-btn
        href="#about"
        text
        class="hidden-sm-and-down"
        @click="onClickMenu"
      >
        <span class="ma-0">About</span>
      </v-btn>

      <v-btn
        href="#faq"
        text
        class="hidden-sm-and-down"
        @click="onClickMenu"
      >
        <span class="ma-0">FAQ</span>
      </v-btn>

      <v-menu offset-y v-if="isMobileView">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="white"
          dark
          v-bind="attrs"
          v-on="on"
          text
        >
          <v-icon>mdi-menu</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item
          v-for="(item, index) in items"
          :key="index"
          :href="item.href"
          @click="onClickMenu"
        >
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
    </v-app-bar>

    <v-main>
      <!-- <HomeView :isHomePage="isHomePage"/> -->
      <div v-if="isHomePage">
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

                <v-btn class="mt-10 pa-6" style="font-size: 20px; color: white; background-color:rgb(228, 113, 36) ;" href="#main" @click="onClickStart">
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
              <v-img class="search" src="./assets/search.png" max-width="50%" />
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="12" id="batas" class="align-center justify-center mt-2">
              <p><b>Be Real . Be Original . Be Authentic</b></p>
            </v-col>
          </v-row>
          <v-row id="faq" class="pt-15">
            <v-col cols="12" md="12" class="d-flex align-center justify-center">
              <h1>FAQ</h1>
            </v-col>
            <v-col cols="12" md="12" class="ml-3">
              <h3>How this application work?</h3>
              <p>This application system works using the Convolutional Neural Network (CNN) algorithm.</p>
            </v-col>
            <v-col cols="12" md="12" class="ml-3">
              <h3>What was the main idea of making this application?</h3>
              <p>Many concerns arise due to the large number of digital image editing applications.</p>
            </v-col>
            <v-col cols="12" md="12" class="ml-3">
              <h3>Is this app paid? </h3>
              <p>No, It's free.</p>
            </v-col>
            <v-col cols="12" md="12" class="ml-3">
              <h3>What is the function of confidence score?</h3>
              <p>Used to show the confidence level of the predicted result.</p>
            </v-col>
          </v-row>
        </div>
      </div>
      <div v-else>
        <div>
          <v-card height="100vh" id="main"> 
          <v-row>
            <v-col cols="12" md="1"> </v-col>
            <v-col cols="12" md="6" class="pa-16">
              <v-card v-if="selectedImage==null" width="100%" height="auto" class="pa-10" style="border-radius:15%; margin-top: -43px;">
                <v-img src="./assets/picture.png" width="100%" heigth="auto"/> 
              </v-card>
              <v-card v-else width="100%" height="auto" class="pa-10" style="border-radius:15%; margin-top: -43px;">
                <v-img :src="url" width="100%" heigth="auto"></v-img>
              </v-card>
            </v-col>
            <v-col cols="12" md="4" class="text-left align-center justify-center" id="container-predict">
              <v-row class="text-left align-center justify-center">
                Confidence Score : {{this.probabilitas}}<br>
                Prediction : {{this.prediksi}}
              </v-row>
              <v-row class="text-center align-center justify-center" style="margin-top:50px;">
                <v-col cols="12" md="3">
                  <v-file-input class="hidden" ref="fileInput" v-model="selectedImage" accept=".png, .jpg, .jpeg" @change="onImageChange"></v-file-input>
                </v-col>
                <v-col cols="12" md="9"> </v-col>
                <v-col cols="12" md="12" class="d-flex align-center justify-center">
                  <div v-if="isPredict">
                    <h5 v-if="showText">
                      Percobaan pertama membutuhkan waktu hampir 1 menit
                    </h5>
                    <v-progress-circular
                      indeterminate
                      color="primary"
                    ></v-progress-circular>
                  </div>
                </v-col>
                <v-col cols="12" md="3"> </v-col>
                <v-col cols="12" md="3">
                  <v-btn @click="onClickInput" style="background-color: rgb(15, 15, 136); color: white;">Input</v-btn>
                </v-col>
                <v-col cols="12" md="3" v-if="selectedImage">
                  <v-btn @click="onClickPredict" style="background-color: rgb(15, 15, 136); color: white;">Predict</v-btn>
                </v-col>
                <v-col cols="12" md="3"> </v-col>
                
              </v-row>
            </v-col>
            <v-col cols="12" md="1"> </v-col>
          </v-row>
          </v-card>
        </div>
      </div>
    </v-main>
  </v-app>
</template>

<script>
// import HomeView from './views/HomeView.vue'
import axios from 'axios'
export default {
  name: 'App',
  // components:{
  //   HomeView
  // },
  data: () => ({
    items: [
        { title: 'Home',href:'#home' },
        { title: 'Contact Me',href:'https://achmadrafifnasution.vercel.app/contact' },
        { title: 'About',href:'#about' },
        { title: 'FAQ',href:'#faq' },
      ],
      isMobileView :false,
      isHomePage:true,
      prediksi:'',
      probabilitas:'',
      isInput:false,
      isPredict:false,
      showText:false,
      timeoutId: null,
      selectedImage: null,
      url:null
  }),
  mounted(){
    this.ResponsiveAppbar()
    window.addEventListener('resize', this.ResponsiveAppbar);
  },
  methods:{
    onClickStart(){
      this.isHomePage = false
    },
    onClickMenu(){
      this.isHomePage = true
    },
    ResponsiveAppbar(){
      const isMobile = window.matchMedia('(max-width: 959px)').matches;
      this.isMobileView = isMobile;
    },
    onClickPredict(){
      this.isInput = false
      this.isPredict = true
      this.timeoutId = setTimeout(() => {
        if (this.isPredict) {
          this.showText = true;
        }
      }, 5000)
      let formData = new FormData()
      formData.append("selectedImage",this.selectedImage)
      axios.post('https://freact-app.onrender.com/api/rafif/freact',formData).then(
        response => {
          this.prediksi = response.data.Prediksi
          this.probabilitas = response.data.Probabilitas
          this.isPredict = false
          this.showText = false
          clearTimeout(this.timeoutId)
        }
      )
    },
    onClickInput(){
      this.isInput = true
      this.prediksi = ''
      this.probabilitas = ''
      this.$refs.fileInput.$refs.input.click();
      // this.$nextTick(() => {
        
      // });
    },
    onImageChange() {
      // const file = event.target.files[0];
      // if (file) {
      //   this.selectedImage = URL.createObjectURL(file);
      //   console.log(this.selectedImage)
      // }
      this.url = URL.createObjectURL(this.selectedImage)
    },
  },
  beforeDestroy() {
    window.removeEventListener('resize', this.ResponsiveAppbar);
  },
};
</script>
<style scoped>
.hidden{
  display: none;
}
#main{
  background-color: rgba(25, 79, 179, 0.986);
}
#home{
  background: url('./assets/latar2.jpg') center center;
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
#batas{
  background-color:white;
  padding-top: 0.5px;
  padding-bottom: 0.5px;
  width:100%;
  text-align: center;
}
#batas p{
  color:rgb(197, 128, 43);
  font-size: 15pt;
  font-family:Georgia, 'Times New Roman', Times, serif;
  word-spacing:8px;
  letter-spacing: 8px;
}
#faq{
  background-color : rgb(0, 65, 130);
  background-image: linear-gradient(to bottom,rgb(0, 65, 130),grey);
  height:100vh;
}
#container-predict{
  padding-top:200px;
}
@media screen and (max-width:600px) {
  #container-predict{
    padding-top:0px;
  }
  #app-name{
    font-size: 200%;
  }
  #batas p{
    font-size: 10pt;
    word-spacing: 3px;
    letter-spacing: 3px;
  }
}
.app{
  overflow-x: hidden;
  overflow-y:hidden;
}
</style>