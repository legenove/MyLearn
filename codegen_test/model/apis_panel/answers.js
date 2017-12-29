/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Answers = function () {
    /*
        @params obj 'data params'
            answer_id   'string' answer id in query
            status   'string' answer status in query
            limit   'integer' limit number
            offset   'integer' offset number
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            status   'string' 
            media_id   'string' 微信media id 三天有效期
            id   'ref' 
            content   'string' 
            voice_url   'string' 保存到七牛的语音地址
            store_type   'string' 
            duration   'integer' 
            date_created   'ref' 
            _voice   'string' 
            voice_id   'string' 
            question_id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/answers",
            method: "GET",
            data: {
                answer_id: obj.answer_id,
                status: obj.status,
                limit: obj.limit,
                offset: obj.offset,
                page: obj.page,
                per_page: obj.per_page
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
    Answers: new Answers
};