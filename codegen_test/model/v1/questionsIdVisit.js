/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var QuestionsIdVisit = function () {
    /*
        @params obj 'data params'
            id   'string' question id in path
            source   'string' 听的来源 付费偷听/好友免费听/分答问/限免听/赞赏听/讨论
            free_key   'string' 
            rewarder_id   'integer' 打赏者id
            
        @success
            status 201    type:object
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/questions/" + obj.id + "/visit",
            method: "POST",
            data: {
                source: obj.source,
                free_key: obj.free_key,
                rewarder_id: obj.rewarder_id
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
    QuestionsIdVisit: new QuestionsIdVisit
};