/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdPublic = function () {
    /*
        @params obj 'data params'
            id   'string' question id in path
            
        @success
            status 200    type:object
            answer   'ref' 
            respondent   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/" + obj.id + "/public",
            method: "GET",
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
    QuestionsIdPublic: new QuestionsIdPublic
};