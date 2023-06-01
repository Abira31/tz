var app = new Vue({
  el: '#app',
  data: {
    data: {
      fam: '',
      password: ''
    }
  },
  methods: {
    login: function () {
     let url = "http://127.0.0.1:5000/api/v1/login"
      fetch(url, {
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(this.data)
      })
        .then(function (response) {
          if (response.status == 200){
            window.location.href = 'http://127.0.0.1:5000/profil'
          }
        })
    }
  }
});
