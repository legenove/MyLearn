/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var GquestionsId = function () {
    /*
        @params obj 'data params'
            id   'string' string id in path
            
        @success
            status 200    type:object
            answer   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/gquestions/" + obj.id + "",
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
    GquestionsId: new GquestionsId
};