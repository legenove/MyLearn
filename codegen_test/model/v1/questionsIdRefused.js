/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdRefused = function () {
    /*
        @params obj 'data params'
            id   'string' question id in path
            content   'string' 
            
        @success
            status 200    type:object
            ok   'boolean' 
            
    */
    this.put = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/" + obj.id + "/refused",
            method: "PUT",
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
    QuestionsIdRefused: new QuestionsIdRefused
};