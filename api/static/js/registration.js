var app = new Vue({
  el: '#app',
  data: {
    data: {
      fam: '',
      im: '',
      ot: '',
      password: ''
    }
  },
  methods: {
    registration: function () {

      let url = "http://127.0.0.1:5000/api/v1/registration"
      fetch(url,
        {
          headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
          },
          method: "POST",
          body: JSON.stringify(this.data)
        })
        .then(function (res) {
         if (res.status == 201){
           window.location.href = 'http://127.0.0.1:5000'
         }

        })
    }
  }
});
