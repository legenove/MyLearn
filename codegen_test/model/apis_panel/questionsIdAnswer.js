/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdAnswer = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            voice_key   'string' 
            
        @success
            status 200    type:object
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/questions/" + obj.id + "/answer",
            method: "POST",
            data: {
                voice_key: obj.voice_key
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
    QuestionsIdAnswer: new QuestionsIdAnswer
};