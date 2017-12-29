/*
 接口定义
 */
var http = require('../../http/base.js');

var app = getApp();

var Talks = function () {
    /*
        @params obj 'data params'
            account_id   'integer' account id in query
            operator_id   'integer' operator id in query
            type   'string' library type in query
            is_sticky   'boolean' is sticky in query
            is_hot   'boolean' is hot in query
            order_by   'string' order by in query
            page   'integer' page number
            per_page   'integer' per_page number
            offset   'integer' offset number
            limit   'integer' limit number
            
        @success
            status 200    type:array
            content   'ref' 
            listenings_count   'integer' 
            operator_id   'ref' 
            account_id   'ref' 
            is_sticky   'boolean' 
            date_updated   'ref' 
            is_active   'boolean' 
            order_score   'integer' 
            _image   'string' 
            share_description   'string' 
            share_title   'string' 
            date_created   'ref' 
            is_hot   'boolean' 
            type   'string' 
            id   'ref' 
            answers_count   'integer' 
            
    */
    this.get = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/talks",
            method: "GET",
            data: {
                account_id: obj.account_id,
                operator_id: obj.operator_id,
                type: obj.type,
                is_sticky: obj.is_sticky,
                is_hot: obj.is_hot,
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
    
    /*
        @params obj 'data params'
            content   'ref' 
            account_id   'ref' 
            is_sticky   'boolean' 
            introduction   'string' 
            is_active   'boolean' 
            order_score   'integer' 
            _image   'string' 
            share_description   'string' 
            share_title   'string' 
            is_hot   'boolean' 
            type   'string' 
            guide   'string' 
            description   'string' 
            
        @success
            status 201    type:object
            content   'ref' 
            listenings_count   'integer' 
            operator_id   'ref' 
            account_id   'ref' 
            is_sticky   'boolean' 
            date_updated   'ref' 
            is_active   'boolean' 
            order_score   'integer' 
            _image   'string' 
            share_description   'string' 
            share_title   'string' 
            date_created   'ref' 
            is_hot   'boolean' 
            type   'string' 
            id   'ref' 
            answers_count   'integer' 
            
    */
    this.post = function (that, obj){
        http.request({
            baseUrl: "/apis/panel",
            url: "/talks",
            method: "POST",
            data: {
                content: obj.content,
                account_id: obj.account_id,
                is_sticky: obj.is_sticky,
                introduction: obj.introduction,
                is_active: obj.is_active,
                order_score: obj.order_score,
                _image: obj._image,
                share_description: obj.share_description,
                share_title: obj.share_title,
                is_hot: obj.is_hot,
                type: obj.type,
                guide: obj.guide,
                description: obj.description
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
    Talks: new Talks
};