/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Voices = function () {
    /*
        @params obj 'data params'
            question_id   'string' question id in query
            account_id   'integer' account id in query
            respondent_id   'integer' respondent id in query
            status   'string' voice filter status in query
            voice_from   'string' voice from in query
            order_by   'string' order by in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            status   'string' 
            respondent   'ref' 
            question_content   'string' 
            asker   'ref' 
            id   'ref' 
            content   'string' 
            voice_url   'string' 保存到七牛的语音地址
            voice_from   'string' 
            _voice   'string' 
            question_id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/voices",
            method: "GET",
            data: {
                question_id: obj.question_id,
                account_id: obj.account_id,
                respondent_id: obj.respondent_id,
                status: obj.status,
                voice_from: obj.voice_from,
                order_by: obj.order_by,
                page: obj.page,
                per_page: obj.per_page,
                offset: obj.offset,
                limit: obj.limit
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
    Voices: new Voices
};