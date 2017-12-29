/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Discussions = function () {
    /*
        @params obj 'data params'
            id   'string' string id in query
            account_id   'integer' account id in query
            respondent_id   'integer' respondent id in query
            question_id   'string' question id in query
            status   'string' status in query
            account_role   'string' account_role in query
            asker_nickname   'string' nickname in query
            respondent_nickname   'string' nickname in query
            order_by   'string' order by in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            voice   'ref' 
            question   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/discussions",
            method: "GET",
            data: {
                id: obj.id,
                account_id: obj.account_id,
                respondent_id: obj.respondent_id,
                question_id: obj.question_id,
                status: obj.status,
                account_role: obj.account_role,
                asker_nickname: obj.asker_nickname,
                respondent_nickname: obj.respondent_nickname,
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
    Discussions: new Discussions
};