/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdTxtAnswer = function () {
    /*
        @params obj 'data params'
            id   'string' question id in path
            content   'string' 
            
        @success
            status 201    type:object
            likings_count   'integer' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/" + obj.id + "/txt_answer",
            method: "POST",
            data: {
                content: obj.content
                },
            success: function (res) {
                typeof obj.success === 'function' && obj.success(res);
            },
            fail: function (res) {
                typeof obj.fail === 'function' && obj.fail(res);
            },
            complete: function (res) {
                typeof obj.complete === 'function' && obj.complete(res);
            }
        })
    };
    

};

module.exports = {
    QuestionsIdTxtAnswer: new QuestionsIdTxtAnswer
};