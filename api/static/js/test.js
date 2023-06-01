

var app = new Vue({
  el: '#app',
  data: {
    data_test : {},
    result_test:[],

  },
  mounted:function (){
    this.get_tests()
  },
  methods: {
    set_none:function(div_test){
        let test_div = document.querySelectorAll("div")
        for (div of test_div){
            if (div.getAttribute("test_id")){
                div.setAttribute("class","d-none")
            }
        }

    },
    get_tests:function() {
      let url = "http://127.0.0.1:5000/api/v1/test"
      fetch(url, {
                method: 'get',
                headers: {
                    'Content-Type': 'application/json',
                },
            })
                .then(response => response.json())
                .then(data => {
                  this.data_test= data
                    let div_app = document.getElementById("test")
                   let count_test = 0
                    let div_test = []
                    let btn_test = document.getElementById("btn_test")
                  for (test of this.data_test){
                      count_test += 1
                      this.result_test.push({"test_id":test.id,"answer":[]})
                      let new_div = document.createElement("div")
                      new_div.setAttribute('test_id',test.id)
                      div_test.push('test_id='+test.id)
                      let p_new = document.createElement("p")
                      p_new.innerHTML = test.text
                      for (answer of test.answer){
                          let new_div_radio = document.createElement("div")
                          let inp = document.createElement("input")
                          inp.setAttribute('_id_test',test.id)
                          if (test.is_many_answer){
                              inp.type = "checkbox"
                          }
                          else{
                          inp.type = "radio"
                          }
                          inp.id='answer_'+answer.id
                          inp.value = answer.id
                          inp.name = 'test_' + test.id
                          let new_lab = document.createElement("label")
                          new_lab.innerHTML = answer.text
                          new_div_radio.appendChild(inp)
                          new_div_radio.appendChild(new_lab)
                          p_new.appendChild(new_div_radio)
                      }
                      new_div.appendChild(p_new)
                      let new_btn = document.createElement("button")
                      new_btn.innerHTML = count_test
                      new_btn.addEventListener("click",function (){
                          app.set_none(div_test)
                          new_div.removeAttribute("class")
                      })
                      div_app.appendChild(new_div)
                      new_div.setAttribute("class","d-none")
                      btn_test.appendChild(new_btn)
                  }
                 but = document.getElementById("btn_test").childNodes[0]
                 but.click()
                })
                .catch((e) => {
                })
    },
    end_test:function (){
        let inputs = document.querySelectorAll("input")
        for (inp of inputs){
            if (inp.checked){
                this.result_test.forEach(element=>{
                if  (inp.getAttribute("_id_test") ==  element.test_id){
                    element.answer.push(parseInt(inp.value,10))
                }
        })
            }
        }
        for (result of this.result_test){
            if (result.answer.length == 0){
                alert('Вы не ответили на все вопросы')
                break
            }
        }

              let url = "http://127.0.0.1:5000/api/v1/test"
      fetch(url, {
                method: 'post',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.result_test)
            })
                .then(function (res){
                    if (res.status == 201){
                        window.location.href = 'http://127.0.0.1:5000/profil'
                    }
                })



    }
  }
})

