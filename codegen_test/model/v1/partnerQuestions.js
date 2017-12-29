/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var PartnerQuestions = function () {
    /*
        @params obj 'data params'
            category   'string' 一点合作 分类
            page   'integer' page number
            per_page   'integer' per_page number
            
        @success
            status 200    type:array
            free_type   'string' 
            category   'string' 
            listenings_count   'integer' 
            respondent   'ref' 
            date_updated   'ref' 
            asker   'ref' 
            is_free   'boolean' 
            content   'ref' 
            url   'string' 
            answer   'ref' 
            type   'ref' 
            id   'ref' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/v1",
            url: "/partner/questions",
            method: "GET",
            data: {
                category: obj.category,
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
    PartnerQuestions: new PartnerQuestions
};