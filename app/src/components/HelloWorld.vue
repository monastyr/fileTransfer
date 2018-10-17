<template>
  <div class="hello">

    <p>CipherText: {{cipherText}} </p>
    <p>Key: {{key}} </p>
    <p>Iv: {{iv}} </p>
    <button v-on:click="getData">get Encrypted Data</button>
    <button v-on:click="decryptData">Decrypt Data</button>
    <button v-on:click="enc">enc</button>
    <button v-on:click="dec">dec</button>

  </div>
</template>

<script>
import axios from 'axios'
import CryptoJS from 'crypto-js'

export default {
  name: 'HelloWorld',

  data () {
    return {
      cipherText: 'dupa',
      iv : '',
      key : '',
      plainText : 'I am batman',
      SECRET: 'password'
    }
  },
  methods:{
    getData: function(){
      axios.post('http://127.0.0.1:8000/encrypted/')
      .then(response => {
        // JSON responses are automatically parsed.
        this.cipherText = response.data.data;
        this.key = response.data.key
        this.iv = response.data.iv
        console.log(this.cipherText);
      })
    },

    enc: function(){

      var b64 = CryptoJS.AES.encrypt(this.plainText, this.SECRET).toString();
      console.log(typeof b64);
      console.log(b64);
      var e64 = CryptoJS.enc.Base64.parse(b64);
      this.cipherText = e64.toString(CryptoJS.enc.Hex);
      console(this.cipherText);
  },

 dec: function(){
   var reb64 = CryptoJS.enc.Hex.parse(this.cipherText);
   var bytes = reb64.toString(CryptoJS.enc.Base64);
   var decrypt = CryptoJS.AES.decrypt(bytes, this.SECRET);
   var plain = decrypt.toString(CryptoJS.enc.Utf8);
  console.log(plain);
},
    decryptData: function(){
      console.log("Decrypt Data")
      // console.log(this.cipherText);)

  //        var reb64 = CryptoJS.enc.Hex.parse(this.cipherText);
  //  var bytes = reb64.toString(CryptoJS.enc.Base64);
  //  var decrypt = CryptoJS.AES.decrypt(this.cipherText, this.key, { 
  //       iv: this.iv, 
  //       padding: CryptoJS.pad.Pkcs7,
  //       mode: CryptoJS.mode.CBC
        
  //     })
  //  var plain = decrypt.toString(CryptoJS.enc.Utf8);
  // console.log(decrypt);

    }
  },
  created(){
    cosnole.log('created');
    //   axios.post('http://127.0.0.1:8000/encrypted/')
    //   .then(response => {
    //     // JSON responses are automatically parsed.
    //     this.cipherText = response.data.data;
    //     this.key = response.data.key
    //     this.iv = response.data.iv
    //     console.log(this.cipherText);
    //   })
    }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
