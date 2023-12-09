<template>
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
            <v-img class="search" src="../assets/search.png" max-width="50%" />
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
      <v-row>
        <v-col>
          ini halaman main
        </v-col>
      </v-row>
    </div>
</template>

<script>
  // import HelloWorld from '../components/HelloWorld'

  export default {
    name: 'HomeView',
    // props:['isHomePage'],
    // components: {
    //   HelloWorld,
    // },
    data(){
      return{

      }
    },
    methods:{
      onClickStart(){
        this.isHomePage = false
      }
    }
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
@media screen and (max-width:600px) {
  #app-name{
    font-size: 200%;
  }
  #batas p{
    font-size: 10pt;
    word-spacing: 3px;
    letter-spacing: 3px;
  }
}

</style>
