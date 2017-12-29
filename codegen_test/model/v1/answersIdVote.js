/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var AnswersIdVote = function () {
    /*
        @params obj 'data params'
            id   'string' answer id in path
            opinion   'string' 暂时只支持投反对票
            
        @success
            status 201    type:object
            ok   'boolean' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/answers/" + obj.id + "/vote",
            method: "POST",
            data: {
                opinion: obj.opinion
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
    AnswersIdVote: new AnswersIdVote
};